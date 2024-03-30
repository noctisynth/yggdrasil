from datetime import datetime
from pathlib import Path
from ipm import exceptions
from ipm.utils import freeze
from ipm.models.ipk import InfiniFrozenPackage
from ipm.api import doc, check, sync, status
from ipm.logging import success, info

import typer
import shutil
import sys
import json

main = typer.Typer(
    name="deploy", help="世界树部署工具", no_args_is_help=True, add_completion=False
)
status.start()


@main.command(
    name="deploy",
    help="世界树部署工具",
)
def deploy(
    package: str = typer.Argument(help="规则包路径"),
    hash: str = typer.Option("", help="哈希值"),
    verify: bool = typer.Option(True, help="验证文件完整性"),
    force: bool = typer.Option(False, "--force", "-f", help="强制重新部署"),
):
    """部署规则包及其文档"""
    info(f"部署规则包...", True)
    status.update("检查世界树环境...")
    if verify and not hash:
        raise ValueError("请先提供文件哈希值以验证文件完整性！")
    cache_path = Path.cwd().joinpath(".deploy-cache")
    cache_path.mkdir(parents=True, exist_ok=True)
    package_path = Path(package).resolve()
    if not package_path.exists():
        raise FileNotFoundError(f"文件 {package} 不存在！")
    if package_path.is_dir():
        raise NotImplementedError("暂不支持部署未打包的规则包项目！")
    success("世界树环境检查完毕。", True)

    status.update("解压缩规则包...")
    project = freeze.extract_ipk(
        package_path, cache_path, hash=hash if verify else None
    )
    success("规则包解压缩成功。")
    status.update(
        f"为 [bold green]{project.name}[/] [bold yellow]{project.version}[/] 处理世界树环境..."
    )
    public_path = Path.cwd().joinpath("public", "packages", project.name)
    public_path.mkdir(parents=True, exist_ok=True)
    target_path = Path.cwd().joinpath(
        "src", "views", "packages", project.name, project.version
    )

    index_path = Path.cwd().joinpath("public", "json", "packages.json")
    index = json.load(index_path.open("r", encoding="utf-8"))
    packages: dict[str, dict] = index["packages"]
    if project.name not in packages:
        packages[project.name] = {}
    packages[project.name]["name"] = project.name
    packages[project.name]["latestVersion"] = project.version
    packages[project.name]["description"] = project.description
    packages[project.name]["authors"] = [
        {"name": author.name, "email": author.email}
        for author in project.authors.authors
    ]
    packages[project.name]["license"] = project.license
    packages[project.name]["topics"] = project.topics
    packages[project.name]["urls"] = project.urls
    packages[project.name]["readme_url"] = f"/packages/{project.name}"
    packages[project.name]["requirements"] = [
        {
            "name": requirement.name,
            "version": requirement.version,
            "yggdrasil": requirement.yggdrasil.index,
        }
        for requirement in project.requirements
    ]
    packages[project.name]["dependencies"] = project.dependencies
    packages[project.name]["lastUpdate"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    distributions: list = packages[project.name].get("distributions", [])
    ifp = InfiniFrozenPackage(package_path, name=project.name, version=project.version)
    for distribution in distributions:
        if distribution["version"] == project.version:
            if not force:
                raise exceptions.ProjectError(
                    f"版本冲突！特定的版本 {project.version} 已经存在！"
                )
            else:
                distribution["readme_url"] = (
                    f"/packages/{project.name}/{project.version}"
                )
                distribution["download_url"] = (
                    f"/packages/{project.name}/{project.default_name}.ipk"
                )
                distribution["hash"] = ifp.hash
                distribution["yanked"] = False
            break
    else:
        distributions.append(
            {
                "version": project.version,
                "readme_url": f"/packages/{project.name}/{project.version}",
                "download_url": f"/packages/{project.name}/{project.default_name}.ipk",
                "hash": ifp.hash,
                "yanked": False,
            }
        )
    packages[project.name]["distributions"] = distributions
    index["packages"] = packages
    success("世界树环境处理完毕。", True)

    status.update("构建文档中...")
    check(project._source_path, echo=True)
    sync(project._source_path, echo=True)
    doc(project._source_path, "vue", target_path, submodule=True, echo=True)
    doc(project._source_path, "vue", target_path.parent, submodule=True, echo=True)
    shutil.copy2(package_path, public_path.joinpath(project.default_name + ".ipk"))
    shutil.copy2(package_path, public_path.joinpath(project.default_name + ".tar.gz"))
    json.dump(index, index_path.open("w", encoding="utf-8"))
    success("文档构建完成。", True)

    status.update("清理环境中...")
    shutil.rmtree(cache_path, ignore_errors=True)
    success("环境清理完成。", True)
    status.stop()


if __name__ == "__main__":
    main()

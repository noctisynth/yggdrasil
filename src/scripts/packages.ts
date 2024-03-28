import packages from "^/packages.json";

interface PackagesInfo {
  [packageName: string]: {
    name: string;
    latestVersion: string;
    description: string;
    authors: { name: string; email: string }[];
    license: string;
    topics: string[];
    urls: {
      homepage: string;
      documentation: string;
      repository: string;
    };
    readme_url?: string;
    requirements: string[];
    dependencies: string[];
    requires_infini: string;
    lastUpdate: string;
    distributions: {
      version: string;
      download_url: string;
      hash: string;
      yanked: boolean;
    }[];
  };
}

const pkgs: PackagesInfo = packages.packages;

export default pkgs;

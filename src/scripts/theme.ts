import { ref } from "vue";

const color_class = ref<string>("bg-primary-600");
const is_light_theme = ref<boolean>(true);

function isLightTheme(): boolean {
  const colorSchemeValue = window
    .getComputedStyle(document.documentElement)
    .getPropertyValue("color-scheme");
  return colorSchemeValue === "light";
}

function changeTheme(PrimeVue: any) {
  if (isLightTheme()) {
    PrimeVue.changeTheme(
      "aura-light-blue",
      "aura-dark-blue",
      "theme-link",
      () => {
        color_class.value = "bg-gray-900";
        is_light_theme.value = false;
      }
    );
  } else {
    PrimeVue.changeTheme(
      "aura-dark-blue",
      "aura-light-blue",
      "theme-link",
      () => {
        color_class.value = "bg-primary-600";
        is_light_theme.value = true;
      }
    );
  }
}

export { changeTheme, color_class, isLightTheme, is_light_theme };

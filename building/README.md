# Building Guide
- Copy the colloid directory to somewhere outside the repo and go that location.
- Copy the color [palette](./whiskers-assets/_color-palette-whiskers.scss) file to colloid/src/sass
- Copy the content from [plank](./plank/) to colloid/src/main/plank
- Copy the content from [assets](./assets/) to colloid/src/assets
- Add the following in [assets.sh](../colloid/assets.sh) and [gtkrc.sh](../colloid/gtkrc.sh) at correct places:
```bash
if [[ "$scheme" == '-Whiskers' ]]; then
    case "$theme" in
      '')
        theme_color_dark='#5284BE'
        theme_color_light='#A5CEFF'
        ;;
      -Purple)
        theme_color_dark='#7D0E70'
        theme_color_light='#FFAAF5'
        ;;
      -Pink)
        theme_color_dark='#7D0E70'
        theme_color_light='#FFAAF5'
        ;;
      -Red)
        theme_color_dark='#B43A2A'
        theme_color_light='#FF8C7C'
        ;;
      -Orange)
        theme_color_dark='#C15D01'
        theme_color_light='#FFB26C'
        ;;
      -Yellow)
        theme_color_dark='#A87B0A'
        theme_color_light='#FFE072'
        ;;
      -Green)
        theme_color_dark='#6A9534'
        theme_color_light='#B1E380'
        ;;
      -Teal)
        theme_color_dark='#5284BE'
        theme_color_light='#A5CEFF'
        ;;
      -Grey)
        theme_color_dark='#502000'
        theme_color_light='#FFECCF'
        ;;
    esac
  fi
```
```bash
-Whiskers)
    background_light='#FFF9F0'
    background_dark='#0E0600'
    background_darker='#0E0600'
    titlebar_light='#FFF3E2'
    titlebar_dark='#0E0600'
    ;;
```

- Add the following in the [install.sh](../colloid/install.sh):
```bash
SCHEME_VARIANTS=('' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin', '-Whiskers')
``` 
```bash
whiskers)
  colorscheme='true'
  schemes+=("${SCHEME_VARIANTS[6]}")
  echo -e "\nWhiskers ColorScheme version! ..."
  shift
  ;;
```
```bash
-Whiskers)
  scheme_color='whiskers'
  ;;
```

- Add the following in [assets.sh](../colloid/src/assets/gtk-2.0/)
```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin' '-Whiskers'; do
```
```bash
if [[ "$type" == "-Whiskers" ]]; then
  background_color='#FFF9F0'
  case "$theme" in 
    '')
      theme_color='#A87B0A'
      ;;
    -Purple)
      theme_color='#7D0E70'
      ;;
    -Pink)
      theme_color='#7D0E70'
      ;;
    -Red)
      theme_color='#B43A2A'
      ;;
    -Orange)
      theme_color='#C15D01'
      ;;
    -Yellow)
      theme_color='#A87B0A'
      ;;
    -Green)
      theme_color='#6A9534'
      ;;
    -Teal)
      theme_color='#5284BE'
      ;;
    -Grey)
      theme_color='#FFECCF'
      ;;
  esac
fi
```
```bash
if [[ "$type" == "-Whiskers" ]]; then
  background_color='#0E0600'
  case "$theme" in 
    '')
      theme_color='#FFE072'
      ;;
    -Purple)
      theme_color='#FFAAF5'
      ;;
    -Pink)
      theme_color='#FFAAF5'
      ;;
    -Red)
      theme_color='#FF8C7C'
      ;;
    -Orange)
      theme_color='#FFB26C'
      ;;
    -Yellow)
      theme_color='#FFE072'
      ;;
    -Green)
      theme_color='#B1E380'
      ;;
    -Teal)
      theme_color='#A5CEFF'
      ;;
    -Grey)
      theme_color='#502000'
      ;;
  esac
fi
```

- Add the following in [make-assets.sh](../colloid/src/assets/xfwm4/make-assets.sh): 
```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin', '-Whiskers'; do
  
```
```bash
if [[ "$type" == '-Whiskers' ]]; then
  headerbar_light='#FFF9F0'
  headerbar_dark='#0E0600'
  headerbar_backdrop_light='#FFF9F0'
  headerbar_backdrop_dark='#0E0600'
  close_color='#FF8C7C'
  max_color='#B1E380'
  min_color='#FFE072'
fi
```

- Add the following in [render-assets.sh](../colloid/src/assets/xfwm4/render-assets.sh): 
```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin' '-Whiskers'; do
```
```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin' '-Whiskers'; do
```

- Add the following in [render-assets.sh](../colloid/src/assets/gtk-2.0/) :
```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin' '-Whiskers'; do
```

```bash
for type in '' '-Nord' '-Dracula' '-Gruvbox' '-Everforest' '-Catppuccin' '-Whiskers'; do
    
```

# Install Script
To make all the whiskers themes
```bash
sh install.sh --tweaks whiskers -l -t yellow teal red purple green orange --dest /tmp/whiskers-gtk-builder;
```
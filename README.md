# dohna:dohna Save&Load helper

An auto clicker driven by PyAutoGUI to load the first save of dohna:dohna.

## Features

* No UAC required.
* Does not affect the memory of the game.
* With a tk GUI, easy to use.
* PyAutoGUI Failsafe enabled, when things comes wrong, move your mouse to the left-top.

## Limitations

* Only tested on M$ Windows 10 x64.
* The game window must be the default size, which also means that this tool does not support games in full screen state.

## TODO

- [ ] 中文文档
- [ ] Multi-Language GUI
- [ ] Status indicator

## Install requirements

```shell
poetry install
```

## Run

```shell
poetry run python bootstrap_win.py
```

## Build release

```shell
poetry run python build-release.py
```

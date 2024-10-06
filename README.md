# Unreal plugin: Python script editor 
A plugin wrapper for Lei Xingyu's [unrealScriptEditor](https://github.com/leixingyu/unrealScriptEditor).

![](https://i.imgur.com/KscixlU.png)

See original [docs](PythonScriptEditor/Content/Python/unrealScriptEditor/README.md)

## Installation
### Plugget install (recommended)
Installation with plugget automatically installs all dependencies. (from the [manifest](https://github.com/plugget/plugget-pkgs/blob/main/unreal/python-script-editor/latest.json))
1. Install the [plugget Unreal plugin](https://github.com/hannesdelbeke/plugget-unreal)
2. Run these 2 Python commands: (in the bottom left of the Unreal editor) 
```python
import plugget
plugget.install("unreal-plugin-python-script-editor")
```

### Manual install
- Copy the unrealScriptEditor folder to your unreal plugin folder. either in your project, or in `C:\Program Files\Epic Games\UE_5.0\Engine\Plugins`, or see [UE plugin docs](https://docs.unrealengine.com/5.0/en-US/plugins-in-unreal-engine/)
- Manually install the dependencies with pip from the `requirements.txt` file
- Start Unreal, and go to the menu `Edit/Plugins`
- Search for `python script editor` and enable the plugin named `python script editor`, do not this confuse with `python editor script plugin`

## Launch tool
- Restart Unreal, if all went well a menu entry should now appear under `Tools/Unreal script editor`

## Community
- unreal forum [thread](https://forums.unrealengine.com/t/free-plugin-python-script-editor/1192090)
- tech-artists.org [thread](https://discourse.techart.online/t/free-plugin-python-script-editor/15918)

## Alternatives
Listing similar products
- https://www.unrealengine.com/marketplace/en-US/product/python-editor
- https://github.com/zkarmakun/PythonEditor

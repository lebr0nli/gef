<p align="center">
  <img src="https://i.imgur.com/o0L8lPN.png" alt="logo"/>
</p>

## pwndbg❤️gef

A patch version of gef to make its commands work with pwndbg without any conflicts.

For everything else than the `gef` prefix commands, we insert a `_` in front of the original command name.

> e.g. `heap chunks` becomes `_heap chunks`

### Installation

```bash
# clone the this repo
git clone --depth 1 https://github.com/lebr0nli/gef.git ~/pwngef
# source it in your ~/.gdbinit
echo -e '\nsource ~/pwngef/gdbinit-pwngef.py\n' >> ~/.gdbinit
```

### For more information

See [hugsy/gef](https://github.com/hugsy/gef) and [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg).

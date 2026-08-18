# helium-browser-bin-opensuse

RPM packaging of [Helium](https://github.com/imputnet/helium-linux) for openSUSE Tumbleweed.

This repackages imputnet's official prebuilt Linux tarball rather than building
Chromium from source. Updated automatically via GitHub Actions when upstream
publishes a new release.

## Install

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:pancakse/openSUSE_Tumbleweed/ helium
sudo zypper refresh
sudo zypper install helium-browser-bin
```

## License

Packaging files (spec, desktop entry, wrapper script) in this repo are MIT
licensed. Helium itself is GPL-3.0 with portions under BSD-3-Clause inherited
from ungoogled-chromium — see [upstream](https://github.com/imputnet/helium-linux)
for details.

Not affiliated with the Helium/imputnet team.

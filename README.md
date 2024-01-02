讀取小米溫溼度計  

``` telegraf
brew install telegraf
ln -sfv /usr/local/opt/telegraf/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.telegraf.plist
```

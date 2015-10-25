### what is this site
This site just copy  from  https://github.com/quokkaproject/quokka

I just want to fix some problem when I need to install to openshift and koding

Fixed Items
1. fix requirements => pyshorteners without any version, becaure 0.5.3 can't be installed
2. need to uninstall Flask-Login then reinstall Flask-Login version to 0.2.11, becaure 0.3.X was
let is_authenticated, is_active, and is_anonymous be property not method
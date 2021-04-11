# Screenshot macro with immediate access to Google Drive

I needed to share screenshots with few other users. To simplify the proccess, I made a script which can make screenshots and then upload them to the common Google Drive folder.

The program is very simple to use. All you need to do is:

- change ID to that of your own google drive folder,
- get `client.secrets.json` from [here](https://console.cloud.google.com/apis/dashboard). You can follow [this tutorial](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf),
- Optionaly, you can set up `settings.yaml` file with your google drive api data, if you don't want to log on Google every time you use it. It's described how to set it up on [this site](https://pythonhosted.org/PyDrive/oauth.html#automatic-and-custom-authentication-with-settings-yaml.).

You are free to use it however you want!

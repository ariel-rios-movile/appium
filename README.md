# Appium

## Installation

## Initial requirements

* Java JDK >=7
* Android SDK
* Python 3 (with virtualenv)
* Node
* NPM

### NodeJS part

```bash
~/appium-movile$ npm install --no-shrinkwrap  # see https://github.com/appium/appium/issues/6978
```

It will install following dependencies:

* Appium framework
* Appium Doctor for environment's requirement checks.

### Python part

```bash
~/appium-movile$ virtualenv env
~/appium-movile$ source env/bin/activate
(env) ~/appium-movile$ pip install -r requirements.txt
```

## Checks environment configuration for Android

```bash
(env) ~/appium-movile$ ./node_modules/.bin/appium-doctor --andriod
```

## Check Android device name

```bash
(env) ~/appium-movile$ adb devices
```

If it does not appear in the list, you must enable debuging options.

## Enabling remote debugging with Chrome

**In your desktop**
  1. Open a Chrome instance and go to `chrome://inspect`
  2. Select associated device on list.

**In your phone**
  3. Allow for remote debugging if not done yet.

## Inspect application with UIAutomator

This tool works analogously to a web inspector; it exposes application UI
composition as XPath value for each element.

```bash
(env) ~/appium-movile$ $ANDROID_HOME/tools/uiautomatorviewer
```

## Test development flow

1. Use remote debugging for web pages or UI inspector for native apps to
   determine the test path to use.
1. Write tests simulating the user's discovery path on the site or application.
1. Validate progress with attached device.
1. Repeat.

### Problems

* Android's fragmentation reduces standarization on native applications, so
  simple tasks as reading SMS text content from UI becomes hard. Custom
  application (or opensource alternatives) as known bindings is a must.
* Very few documentation, or distributed along the official pages for each tool
  in the Appium's chain of responsability.
* Requires existent devices to be attached to computer running tests.

## Visible benefits

1. Complete full integration tests.
1. Repeatable. Documentable.
1. Available on multiple programming languajes.

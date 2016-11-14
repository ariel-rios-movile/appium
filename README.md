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

## Test development flow

1. Use remote debugging to determine the test path to use (CSS selectors,
   classes, names or XPath).
1. Write tests simulating the user's discovery path on the site.
1. Validate progress with attached device.
1. Repeat.

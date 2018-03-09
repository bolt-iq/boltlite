# [<img src="http://www.boltiq.io/wp-content/uploads/2018/01/BOLTBig-174x100.png" alt="Flutter" width="174" height="100" />](http://www.boltiq.io)
[![Join Gitter Chat Channel -](https://badges.gitter.im/flutter/flutter.svg)](https://gitter.im/BOLT-IQ/Community)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/boltiq_io)


<img src="http://www.boltiq.io/assets/boltlite.gif" alt="Intelligent Quality">

BOLT Lite is an automated testing library to help developers, QA, and business start building an automated testing suite in less time and at a lower cost. BOLT Lite is the free version of BOLT Test, providing a way for teams to get started in Automation. The full version of BOLT comes with a suite of integrations and features to build out a full automation suite. This repo provides the BOLT Lite library along with an environment setup to start building tests immediately. There are also a few sample specs included to show how tests are created within BOLT. As BOLT Lite is free, there are many features that have been restricted and/or removed. A full list of features is provided below.

## Technical Overview for Developer, Automation Engineer, SDET, and technical individuals
BOLT Test is a library designed to take the difficulty out of implementing automation for a project. BOLT Test is already designed and takes out a lot of the guess work in building a new automated test framework. This library contains the setup for Appium and Selenium including driver creation for local and remote testing across multiple browsers. Beyond just that setup, there are actions created to use Appium and Selenium for getting elements, clicking elements, sending text, etc. There are also many steps that have are included with BOLT Test allowing those actions to be utilized in tests. BOLT Test has also been integrated with JMeter, SoapUI, Hibernate and JPA, Spring API, and more. This makes it very easy to run and manage all tests (UI, API, Performance) within one location using specs. This also makes it easy to make API and database calls for validation. Hibernate/JPA and Spring make the process incredibly easy for making API and database calls. If you aren’t experienced with these two systems, they use objects (created for the different calls/responses) to send information and/or can populate objects with the response from the call. This eliminates the need for old-school parsing of responses. BOLT Test is designed to be modular making it easy to extend BOLT Test to do whatever is needed or incorporate any integration. 


## Features

Not all features are available on the BOLT Test Lite version. A full list of features including a description can be found in the Feature List.docx file.

* Pre-Built library of selenium actions
* Pre-Built library of test steps
* Pre-Built spec files
* Pre-Built support for API calls using Spring
* Pre-Built support for database calls using JPA
* Integrated with Selenium for web testing
* Integrated with Appium for mobile and desktop testing
* Integrated API testing through JMeter and SoapUI
* Support for adding custom actions and steps
* Support for negative testing
* Support for custom element definitions and effective management of them
* Support for multiple reporting types. HTML, XML, Spectacle, and Flash.
* Support for most browsers and devices
* Support for headless testing through phantomjs and chrome
* Support for parallel test execution
* Property files for different environments

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Specs built on BOLT Lite can be used directly with BOLT without any re-working required.

Instructions with links are also available at [boltiq.io](http://www.boltiq.io/bolt-lite/)

### Prerequisites

#### Container Running Prerequisites

1. Docker [Docker Install Instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (Select your environment on the left)


#### Local Running Prerequisites

1. Java 8 [Install instructions](https://www3.ntu.edu.sg/home/ehchua/programming/howto/JDK_Howto.html)
2. Intellij (community edition) [Install instructions](https://www.jetbrains.com/idea/download/)
3. Gauge [Install instructions](https://gauge.org/get-started.html)
4. Gauge plugin for Intellij [Install instructions](https://docs.gauge.org/using.html#intellij-idea)


#### Appium Prerequisites

1. Appium
2. Appium server or an external source (custom server, browserstack, etc)

Emulator Testing
1. xcode and/or Android Studio
2. Installed device(s) and operating system(s) for emulator

Real Mobile Device Testing
1. Real device


### Installing

#### Install BOLT Test Container

1.  Run docker pull boltiq/boltlite:latest
2.  Run docker run --name boltlite -v /home/bolt/code:/src -p 5901:5901 boltiq/boltlite:latest
3.  Edit the location "/home/bolt/code/" to a known local location or create the provided directory path
4.  VNC into the container using your docker IP and port 5901 (The default VNC password is password)
5.  Go to your local volume location "/home/bolt/code"
6.  Git Clone "https://github.com/bolt-iq/boltlite" (you can also donload ZIP and unzip the contents to your local volume location)
7.  Open VNC and launch IntelliJ (The default VNC password is password)
8.  The BOLT project will be loaded and indexed.
9.  Open specs/demo/demo.spec and run it to verify the successful installation
10. Chrome Browser should open and run the spec.

#### Install BOLT Test locally

1.  Clone the BOLT Test sample project from [GitHub] (https://github.com/bolt-iq/boltlite)
2.  Open Intellij and open the project that was just cloned from github.
3.  Allow IntelliJ to install the maven dependency.
4.  Open specs/demo/demo.spec and run it to verify the successful installation
5.  Chrome Browser should open and run the spec.

### Create Your First Test
BOLT Test comes preconfigured to point at boltiq.io and this will walk through creating a simple test for this site.
1.  Create a new spec within the "specs/demo/" folder by right clicking the demo folder and selecting "New > Specification" and name the file. This creates a base spec to start working with.
2.  Change the Specification Heading to "BOLTIQ_Demo_Spec".
3. Add a line before "Scenario Heading" that looks like "* Go to AUT"
4. Change "Scenario Heading" to "BOLTIQ Demo Test"
5. Under the Scenario Heading line, add a new line "* Navigate to "Features""
6. Use the green play button next to the spec heading and select "Run 'BOLTIQ_Demo_Spec.spec'"
7.  Watch Bolt initialize, open Chrome, navigate to the AUT (which is boltiq.io), and navigate to the Features tab. 

## Writing tests

Tests are written in files called specification (spec) files. A spec file will contain the tests for either a single page or a single feature. To cover negative tests, a second spec should be written for each page or feature and the title should end with "-NEGATIVE" to identify it as a negative test. This will disable much of the default validation that is built into BOLT Test to help prevent unintended test failures.

Often, there will be a series of steps that is the same for many different tests. To reduce the risk for boredom, carpal tunnel, and to reduce the number of steps, there are a few ways that this repetition can be reduced. The first is by using setup and teardown steps. Setup steps are written before the first test in a spec file. These steps will be run before every test in that spec. Teardown steps are written at the end of a spec file after a line containing only "---" and these steps will be run after every test in the given spec. In addition to setup and teardown steps, multiple steps can be combined using a concept file. A concept file can contain many groupings of steps within one file. Concepts can take in variables and need to be given unique names. When using a concept in a test case, simply start writing the step as any other and just use the unique name for the concept instead of a step.

When writing tests, tags can be added to a spec file, or to just a specific test, to group/categorize tests. When running tests via command line, a single (or multiple) tags can be specified and only tests with the given tag(s) will be run. This can be very helpful for marking tests as regression tests, smoke tests, performance tests, etc.

To get a better understanding of how to write tests, please look at the demo spec files designed to show these features.

## Running the tests
### Running tests in IntelliJ
The easiest way to run BOLT tests is directly through IntelliJ. Tests can be run either on the spec level or on the test case level within IntelliJ. When looking at a spec, there is a green arrow next to the line numbers. These arrows open a menu allowing the selection to be run, debugged, or run with coverage. The arrow next to the spec heading (on line 1) will run all tests within the spec and the other arrows will simply run the test case they are next to. When running a single test case, it will run through multiple times if it is reading from a set of data, else it will only be run once.
### Running tests from command line

To run via command line, navigate to the home directory for BOLT Test. To determine the exact command, use the
following table:

|Command/configuration     |Description
|---------------------------|------------------
|mvn gauge:execute         |Primary Command
|-DspecsDir=               |A specific spec or folder of specs can be specified to run
|-DinParallel=             |“true or false”, specifies to run in parallel or not.
|-Dnodes=                  |The maximum number of nodes to use. Uses all nodes if not included.
|-Dtags=                   |“tag1 & tag2” Run tests only with the given tag(s).
|-Denv=                        |How to specify what environment to run the tests against.
|-Ddir=                        |Working directory for gauge. Default is project.base.dir
|-Dflags=””                    |Add additional flags to the execution


## Runtime Report
While BOLT Test is executing, there is a flash report that can be monitored to see what test(s) are running and if they have passed or failed. It does not contain the detailed information of the HTML Report, but it can provide an idea of what stage the tests are at and how successful they have been. To use this report, flash must be an installed plugin for gauge. To install flash, open command line and type "guage install flash" and hit enter. Then, in the project, open the manifest.json file and add "flash" to the list of Plugins.

## HTML Report
After each execution of tests on BOLT Test is completed, an HTML report is generated with the results. This report opens to a summary page showing the number of specs that passed or had failures. By selecting a spec, the step-by-step results can be observed for each test. In the case of data-driven tests, a table will be displayed and by selecting each row, the step-by-step results can be observed. When a step fails, a screenshot will be attached to the failed step along with the reason for the failure.

## Properties
There are many properties that can be defined in the property files to specify the application under test, browser, bug reporting, and much more. Below is a complete list of the options for the properties file.
Some of these options are only for the paid version of BOLT Test and they are defined. For information on cost, please visit [BOLTIQ](http://www.boltiq.io)

|Property                          |Description                                                                                                |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------|
|REMOTE_SYSTEM                     |Defines which remote system to be using, saucelabs, browserstack, or openshift.                            |
|BROWSER                           |Defines the browser to test within.                                                                        |
|BROWSER_VERSION                   |Available to specify a specific browser version. Selects the latest available version if empty.            |
|REMOTE                                |True to run on the defined remote system                                                                   |
|REMOTEURL                         |Default remote system url to use if remote_system is empty                                                 |
|BROWSERSTACK_URL                  |URL to connect to for a browserstack test run                                                              |
|SAUCELABS_URL                     |URL to connect to for a saucelabs test run                                                                 |
|OPENSHIFT_URL                     |URL to connect to for an openshift test run                                                                |
|ELEMENT_DEFINITIONS               |File location of the element definitions csv file                                                          |
|ELEMENT_WAIT_TIME                 |Maximum time to wait for an element                                                                        |
|IP                                    |IP address of the AUT (used for JMeter testing)                                                            |
|PORT                              |Port of the AUT (used for JMeter testing)                                                                  |
|AUT_URL                           |URL of the AUT (Application Under Test)                                                                    |
|BUTTON_TYPE                       |WebElement type of buttons in the AUT                                                                      |
|LABEL_TYPE                            |WebElement type of labels in the AUT                                                                       |
|SPECIAL_TEXT_ATTRIBUTE                |WebElement attribute for element text if text is stored in an attribute instead of in a standard manor.    |
|PAGE_HEADING_LEVEL                    |Heading level of the page titles (h1,h2,h3, etc)                                                           |
|TEXT_FIELD_TYPE                   |WebElement type of text fields                                                                             |
|TEXT_AREA_TYPE                        |WebElement type of text areas                                                                              |
|CHECKBOX_TYPE                     |WebElement type of checkboxes                                                                              |
|FIELD_DEFAULT_FIELD_ATTRIBUTE     |WebElement attribute of text field default values                                                          |
|TEXTAREA_DEFAULT_FIELD_ ATTRIBUTE |WebElement attribute of text area default values                                                           |
|INITIAL_AUT_LOAD_TIME_MS          |Optional wait for initial loading of the AUT                                                               |
|FLASH_SERVER_PORT                 |Port for the flash report to persist upon                                                                  |
|REMOTE_HOST_#                     |Location of remote nodes to use with jmeter testing.                                                       |
|REPORT_TO_JIRA                        |true to report bugs/failures to jira                                                                       |
|JIRA_URL                          |the domain for jira (https://your_domain.atlassian.net)                                                    |
|JIRA_PROJECT_ID                   |the id of the project to report bugs to                                                                    |
|JIRA_AUTHORIZATION                    |username:password encoded with base64 for the user automation will use to report bugs                      |
|JIRA_SECONDS_BETWEEN_COMMENTS     |Adds comments to a bug only if there was no activity on the bug for this number of seconds                 |


|DB.PROPERTIES         |Properties for pulling data from a database to use for specs.  |
|-----------------------|---------------------------------------------------------------|
|QUERY_#               |The query to make ('#' is the index starting at 1)             |
|FILENAME_#                |The filename to store the query results                        |
|PERSISTANCE_UNIT      |The persistanceUnit to use for all queries unless overridden   |
|PERSISTANCE_UNIT_#        |The persistanceUnit to use for a given query                   |


|Appuim.properties         |Properties for appium                                              |
|---------------------------|-------------------------------------------------------------------|
|RUN_WITH_APPIUM           |True to run tests using appium                                     |
|APP_LOCATION              |Location of the app under test (leave empty if testing webapp)     |
|MOBILE_BROWSER                |Browser to use for appium testing                                  |
|MOBILE_BROWSER_VERSION        |Browser verison to use for appium testing                          |
|AUT                       |Url for the AUT on mobile                                          |
|PLATFORM                  |iOS or Android                                                     |
|PLATFORM_VERSION          |Version of iOS or Android                                          |
|DEVICE_NAME               |Name of the device to test                                         |
|REAL_MOBILE               |True for testing on a real device (for use with external services) |
|APPIUM_SERVER             |Location of the appium server (or external service)                |
|APPIUM_VERSION                |Version of appium to test (optional)                               |


## Building custom steps

BOLT Test is designed to be expanded upon and customized for each client as it is impossible to predict every situation that needs to be tested. If a step is needed that does not already exist, a custom step can easily be built for the task. There is a folder named "CustomSteps" which contains a starting point/example for adding custom steps.

At the start of the new Java class, an object will need to be created for either "SeleniumSmartActions" and/or whatever custom action classes which have been built. From this point, a method for the new step can be built to complete whatever task is needed. As a note, it is not recommended to use webdriver in this class. All direct interactions with the browser using Selenium webdriver should be contained within an existing or custom action method/class. After creating the method to complete the task that is needed, the method needs to be turned into a step. This is done by adding "@Step("insert step here with a <variable>")" directly before the method. Variables are surrounded by '<>' and are passed into the method. It is recommended to keep the same variable names and order from the step definition and the method parameters.

## Building custom actions

BOLT Test is designed to be expanded and customized by each client as it is impossible to predict every situation that needs to be tested. If an action does not currently exist in BOLT Test, a custom action can easily be built to do anything. There is a folder named "CustomActions" which contains a starting point/example for adding custom actions and steps.

When creating a new custom action class, the class should either extend an existing action class, or contain an object of one of the action classes. If extending an action class, a webdriver object will be available due to extending the class. If that is not the case, a local webdriver object will need to be created.

From this point, new methods can be created that use the webdriver and existing methods from SeleniumSmartActions to complete any task required.

## Deployment

This system is designed for use with a CI/CD development process to aid in testing software and catching bugs before software is released. BOLT Test can run locally or on a fully automated CI/CD pipeline.

## Built With

* [Gauge](http://gauge.org) - The test building framework
* [Selenium](http://www.seleniumhq.org) - The tool to directly interact with a browser
* [JMeter](http://jmeter.apache.org) - The primary API and Performance testing tool
* [Maven](https://maven.apache.org/) - Dependency Management

## Contributing
This is not an opensource project, BOLT Test Lite is a free version of [BOLT Test](http://www.boltiq.io). If issues or bugs are found, please checkout the [forum](), [chat](), and existing bugs on [github](https://github.com/bolt-iq/boltlite/issues).


## Versioning

We use a private Maven server for versioning. To pull the BOLT Test Library from this server, there is a username and password already provided for the free version.
To use the full version, please go to the [BOLT Website](http://www.boltiq.io) for purchasing information.

## Authors

* **Swat Solutions** - *Built and maintains*


## License

BOLT Lite is proprietary software - please refer to the BOLT License.txt file for all information regarding licensing. 
For the full version of BOLT Test, please refer to the (www.boltiq.io) website for pricing information.

## Acknowledgments
* [Selenium](https://www.seleniumhq.org)
* [Appium](http://www.appium.io)
* [Gauge](https://gauge.org)
* [JMeter](http://jmeter.apache.org)
* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)


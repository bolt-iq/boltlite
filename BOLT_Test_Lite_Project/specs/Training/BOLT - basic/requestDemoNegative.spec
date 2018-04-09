RequestDemo-Negative
====================

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

These tests are expected to get an error message upon clicking send as the email is missing for both test cases

* Go to "http://boltiq.io"

Submit Request Missing Email and Company Name Fail Expected
-----------------------------------------------------------
* Verify page title matches "Intelligent Quality"
* Enter text "Bob" into field with default value "Name"
* Enter text "" into field with default value "Email Address"
* Enter text "" into field with default value "Company Name"
* Click "Send" button
* Verify page title matches "FAIL HERE"

Submit Request Missing Email Only
---------------------------------
* Verify page title matches "Intelligent Quality"
* Enter text "Bob" into field with default value "Name"
* Enter text "" into field with default value "Email Address"
* Enter text "Bob Industries" into field with default value "Company Name"
* Click "Send" button
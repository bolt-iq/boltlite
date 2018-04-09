Add To Cart Tests
=================

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

    table:specs/Training/AutomationPractice - advanced/options.csv


 Go to AUT
 * Go to "http://automationpractice.com/index.php"

Add Shirt to Cart
-----------------
 Hover over "WOMEN" tab
* Hover over "WOMEN" tab and select "Evening Dresses"
* Click "Beige (1)" checkbox
* Click "Printed Dress"
* Select "M" from the "Size" dropdown
* Click "Add to cart" button
* Click "Proceed to checkout"
Delay to show the checkout screen
* Delay "3" seconds
* Click defined symbol "LOGO"


Add Shirt to Cart Using Table
-----------------------------
 Hover over "WOMEN" tab
* Hover over "WOMEN" tab and select <Category>
* Click <Filter> checkbox
* Click <Shirt>
* Select <Size> from the "Size" dropdown
* Click "Add to cart" button
* Click "Proceed to checkout"
* Click defined symbol "LOGO"

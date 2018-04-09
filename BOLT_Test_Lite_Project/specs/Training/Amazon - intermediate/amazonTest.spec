Quick Amazon Test
=================

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

     |product       |
     |--------------|
     |Fire HD 8     |
     |Fire HD 10    |

* Go to "http://www.amazon.com"

Add Fire product to cart
------------------------
* Hover over "Departments" tab
* Click text "Fire Tablets"

This step is utilizing the table above and this test will be run once per entry into the tabel
* Click text <product>
* Click "Add to Cart" button
* Delay "1000" milliseconds



Add Fire TV to cart
-------------------
* Hover over "Departments" tab
* Click text "Fire TV"
* Click text "Fire TV Stick"
* Click "Add to Cart" button
* Delay "1000" milliseconds



---
Clicking the x on the popup using the element attribute "aria-label" matching "Close"
* Click element with attribute "aria-label" and value "Close"

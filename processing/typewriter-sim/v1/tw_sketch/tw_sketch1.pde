PFont myFont;
String myText = "Lorem ipsum";

void setup()
{
  int paperlen = 842 * 8;
size(595,842); // size of output window in pxels (width, height)
background(100); // grayscale, 255 is white 0 is black
myFont = loadFont("AmericanTypewriter-48.vlw"); // create a font object
// using a specified font
textFont(myFont, 48); // the first argument is the font to use
// the second argument is the font size
noLoop(); // no loop; only executs the draw function once
}

void draw()
{
fill (0); // specify the font color in grayscale, 255 is white and
// 0 is black
text(myText,30,110); // the first argument is a string specifying
// the text to display
// the second and third arguments are the x and y positions in pixels
// from top left to bottom right specifying where to start typing
}

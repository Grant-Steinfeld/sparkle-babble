PFont font;

String FILE_NAME = "../data/hex-seti/seti-freq_504_.txt";
String[] lines = null;
String ss = null;

String[] getListOffFile(){
   return loadStrings(FILE_NAME);
}

void setup() {
  size(495, 942);
  // A4 dimensions https://www.google.com/search?client=firefox-b-1-d&q=pixel+height+and+width+A4+paper
  frameRate(1);
  smooth();
  font = createFont("Courier", 8); //want fixed width font!
  lines = getListOffFile();
  setLinesAsString(lines);
  textFont(font, 12);
}

void setLinesAsString(String[] lines)
{
   ss = new String();
   for (int i = 0 ; i < lines.length; i++) {
      ss =ss + lines[i] + "\r\n";
   }
}

void draw() {
  fill(0);
  int x = 1;
  int y =100;
  text(ss,x,y);
  noLoop();
}

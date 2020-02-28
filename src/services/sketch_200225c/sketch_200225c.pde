

PFont font;
int counter = 0;


 String[] getListOffFile(){

 return loadStrings("../data/seti-freq_504_.txt");


}

  String[] lines = null;
  String ss = null;

void setup() {
  //background(150);
  size(495, 942);
  //https://www.google.com/search?client=firefox-b-1-d&q=pixel+height+and+width+A4+paper
  frameRate(1);
  smooth();
  font = createFont("Courier", 8);
  //font = loadFont("IBMPlexSerif-48.vlw");
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

  //background(150);
  fill(0);


  int x = 1;
  int y =100;


    text(ss,x,y);
    noLoop();


}

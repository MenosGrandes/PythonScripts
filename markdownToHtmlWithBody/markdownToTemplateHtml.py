import markdown
import codecs
import sys, getopt

def main(argv):
    
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print ('markdownToTemplateHtml.py -i <inputfile> -o <outputfile>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print ('markdownToTemplateHtml.py -i <inputfile> -o <outputfile>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
    print( 'Input file is "', inputfile)
    print( 'Output file is "', outputfile)
       
       
       
    input_file = codecs.open(inputfile, mode="r", encoding="utf-8")
	
    text = input_file.read()
    input_file.close()
    html = markdown.markdown(text,extensions=["abbr" , "nl2br" ,"sane_lists" ,"def_list"])
    
    output_file = codecs.open(outputfile, "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    htmlTemplate ="""
    <!doctype html>
    
    <html lang="en">
    <head>
      <meta charset="utf-8">
    
    
      <link rel="stylesheet" href="{css}">
    
    </head>
    <body>
    {markdown}
    </body>
    </html>
    
    """.format(markdown = html, css = "css/retro.css")
    output_file.write(htmlTemplate)
    output_file.close()
    print("done")
 
 
 
if __name__ == "__main__":
   main(sys.argv[1:])
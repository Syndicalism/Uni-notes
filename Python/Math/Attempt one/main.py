import os;
import json;
#import jsbeautifier;

def flagError( message ):
    print("CRITICAL ERROR:",message)
    input("!!!!!!!!!!!!!!!!!!!")

def getPath():
    return os.path.dirname(os.path.dirname(__file__))+"\\"+"Equations"

class Equation:
    parentEC = -1;
    rawJSON = -1;
    topicName = ""
    filePath = ""

    name = ""
    eqString = ""
    desc = ""
    variableSymbols = []
    path = []

    variables = []

    def __init__(this, parentEC, name, JSONInp, topicName ):
        this.rawJSON = JSONInp
        this.parentEC = parentEC
        this.topicName = topicName
        this.filePath = this.parentEC.tPaths[ topicName ]

        this.variableSymbols = JSONInp["vars"]
        this.name = name
        this.eqString = JSONInp["eq"]
        this.desc = JSONInp["desc"]

        if name in parentEC.parentEF.allEquations:
            flagError( "duplicate of '"+name+"' equation!" )
        
        parentEC.parentEF.allEquations[ name ] = ( this )

        return

    def genHash(this):
        return hash(  this.name + this.eqString + "- -".join(str(x) for x in this.variableSymbols) )
    
    def checkConfigured(this):
        if "hash" in this.rawJSON:
            cHash = this.rawJSON["hash"];

            nHash = this.genHash();

            if ( cHash != nHash ):
                print("change detected in:",this.name)
                this.getConfiguration()

        else:
            this.getConfiguration()
    
    def getConfiguration(this):
        print( "\n\n'"+this.name+"' is not set up properly, equation:"+this.eqString )
        print("Description:",this.desc)
        print("Link it's variables.\n")

        errorHit = False;

        for variable in this.variableSymbols:
            vObj = this.parentEC.parentEF.findVarSymbMatch( variable, this );
            if ( vObj == False ):
                errorHit = True
            
            this.variables.append( vObj )
        
        if ( errorHit ):
            flagError("yep stop it")
            return;

        this.saveChanges( );

        return;

    def construct(this):
        
        #this.checkConfigured();



        return;
    
    def saveChanges(this):
        return;
        nHash = this.genHash();
        
        cFile = open( this.filePath, "r" );
        cJSON = json.loads( cFile.read() );
        cFile.close()

        varNames = []
        for var in this.variables:
            varNames.append( var )

        cJSON["equations"][this.name]["hash"] = nHash;
        cJSON["equations"][this.name]["mVars"] = varNames;

        #opts = jsbeautifier.default_options()
        #opts.indent_size = 2

        #cFile = open( this.filePath, "w" );
        #cFile.write( jsbeautifier.beautify(json.dumps(cJSON), opts) )
        #cFile.close()

        return
        

class Variable:
    parentEC = -1;

    name = ""
    symbol = ""
    isConstant = False
    constValue = 0
    desc = ""
    path = []

    equations = []
    filePath = ""

    def __init__(this, parentEC, name, JSONInp, filePath):
        this.filePath = filePath;
        this.parentEC = parentEC;

        this.name = name;
        this.symbol = JSONInp["symbol"]
        this.desc = JSONInp["desc"]

        if ( "value" in JSONInp ):
            this.isConstant = True
            this.constValue = JSONInp["value"]

        this.addToMainThing();

    def stringInfo( this, indent ):
        return(
            indent + "name: "+ this.name + "\n"+
            indent + "desc: "+ this.desc + "\n"+
            indent + "path: "+ ",".join(str(x) for x in this.path)
        )

    def addToMainThing(this):
        if this.name in this.parentEC.parentEF.allVarnames:
            flagError(this.name,"has a duplicate variable name!")
        else:
            this.parentEC.parentEF.allVarnames.append( this.name )


        if not this.symbol in this.parentEC.parentEF.allVariables:
            this.parentEC.parentEF.allVariables[this.symbol] = []
        
        this.parentEC.parentEF.allVariables[this.symbol].append( this )

        if ( this.isConstant ):
            if not this.symbol in this.parentEC.parentEF.allConstants:
                this.parentEC.parentEF.allConstants[this.symbol] = []
            
            this.parentEC.parentEF.allConstants[this.symbol].append( this )

    
        
  
class EqCatagory:
    parentEF = -1

    topics = {}
    tPaths = {}

    desc = ""
    name = ""
    variables = []

    def __init__(this, parentEF, JSONInp ):
        this.parentEF = parentEF;
        this.name = JSONInp["dir"];

        path = getPath() + "\\" + this.name + "\\"
        
        for i in range(0, len( JSONInp["subs"] ) ):
            sub = JSONInp["subs"][i]
            fContents = open( path + sub + ".json" , "r").read() 
            tmp = json.loads( fContents )

            this.tPaths[ sub ] = path + sub + ".json"

            this.loadVars( tmp["variables"], path + sub + ".json" )
            this.loadTopic( sub, tmp["equations"] )

        
        return;

    def loadVars( this, JSONinp, filePath ):
        
        for varName in JSONinp:
            this.variables.append( Variable( this, varName, JSONinp[varName], filePath )  )

        return;

    
    def loadTopic(this, name, JSONInp):
        if name in this.topics:
            flagError( name + " already exists warning!" )
        
        eqs = {};

        for eq in JSONInp:
            eqs[ eq ] = Equation( this, eq, JSONInp[eq], name )


        this.topics[ name ] = eqs

    def construct( this ):
        
        return;




class EquationFetcher:
    rootJSON = ""

    allEquations = {}
    allVariables = {}
    allConstants = {}

    allVarnames = []

    eqCatagorys = {}

    def findVarSymbMatch( this, symbol, requestSource ):
        if ( symbol in this.allVariables ):
            matches = this.allVariables[symbol];

            print("The variable(s) found for the symbol \""+symbol+"\" are:")

            for i in range(0, len(matches) ):
                print(i,":")
                print( matches[i].stringInfo("  "),"\n" )
            
            print("Select the right one or type -1 if you need to create a new variable")
            inp = ""
            invalidInp = True
            while ( invalidInp ):
                inp = input("Input: ")

                if ( input("Confirm choice(y/n): ") == "y" ):
                    invalidInp = False

            if ( inp == "-1" ):
                return this.createVariableInp( symbol, requestSource )
            else:
                return matches[  int( i ) ];
        else:
            return this.createVariableInp( symbol, requestSource );

    def createVariableInp( this, symbol, requestSource  ):
        input("no appropriate variable for the symbol \""+symbol+"\"")
        return False;
        flagError("shit!")
        print("leave value blank if it isn't a constant")
        while ( True ):
            name   = input("name : ")
            desc   = input("desc : ")
            value  = input("value: ")
            if ( input("Confirm choice(y/n): ") == "y" ):
                return this.createVariable( symbol, name, desc, value, requestSource );

    def createVariable( this, symbol, name, description, value, requestSource ):
        if name in this.allVarnames:
            flagError("You absolute retard")

        path = requestSource.parentEC.tPaths[ requestSource.topicName ];

        cFile = open( path, "r" );
        cJSON = json.loads( cFile.read() );
        cFile.close()

        cFile = open( path, "w" );
        #cFile.write( cJSON )
        cFile.close()

        return;



    def __init__(this):
        print("init")
        this.getRootJson();
        print( this.rootJSON );
        this.generateEqCatagorys()
    
    def getRootJson(this):
        rFile = open( 
            getPath() + "\\Equations.json"
        )
        this.rootJSON = json.loads( rFile.read() )
        rFile.close();

    def generateEqCatagorys(this):
        locations = this.rootJSON["locations"]

        for i in range(0, len(locations)):
            location = locations[i]
            if ( location["dir"] in this.eqCatagorys ):
                flagError( location["dir"] + " is a duplicate topic name!")

            this.eqCatagorys[ location["dir"] ] = EqCatagory( this, location ); 

        print("all vars:", this.allVariables.keys() )

        for catagory in this.eqCatagorys:
            this.eqCatagorys[catagory].construct()

        for equation in this.allEquations:
            this.allEquations[equation].construct()
        

        



def count_sub_in_file( filename, s ):
    return open( os.path.dirname(__file__) + "\\" +filename, "r" ).read().count( s );



tmp = EquationFetcher();

print(getPath());
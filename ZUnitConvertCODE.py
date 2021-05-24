conversion_dict = {
    "length": {
        "meters": {
            "meters": lambda x: x,
            "yards": lambda x: 1.0936 * x,
            "feet": lambda x: 3.28084 * x,
            "centimeters": lambda x: 100 * x,
            "kilometers": lambda x: x / 1000.0,
            "miles": lambda x: x / 1000.0 / 1.60934
        },
        "yards": {
            "yards": lambda x: x,
            "meters": lambda x: x / 1.0936,
            "centimeters": lambda x: x / 1.0936 * 100,
            "feet": lambda x: 3 * x,
            "kilometers": lambda x: 0.0009144 * x,
            "miles": lambda x: 0.0009144 * x / 1.60934
        },
        "centimeters": {
            "centimeters": lambda x: x,
            "meters": lambda x: x / 100.0,
            "yards": lambda x: x * 1.0936 / 100,
            "feet": lambda x: x * 3.28084 / 100,
            "miles": lambda x: x * 100 * 1000 / 1.60934
        },
        "feet": {
            "feet": lambda x: x,
            "meters": lambda x: x / 3.28084,
            "yards": lambda x: x / 3.0,
            "centimeters": lambda x: x * 100 / 3.28084,
            "kilometers": lambda x: x * 3.28084 / 1000,
            "miles": lambda x: x * 3.28084 / 1000 / 1.60934
        },
        "miles": {
            "miles": lambda x: x,
            "kilometers": lambda x: 1.60934 * x,
            "meters": lambda x: 1.60934 * x * 1000,
            "centimeters": lambda x: 1.60934 * x * 1000 * 100,
            "feet": lambda x: 5280 * x,
            "yards": lambda x: 5280 * x / 3.0
        },
        "kilometers": {
            "kilometers": lambda x: x,
            "meters": lambda x: x * 1000,
            "centimeters": lambda x: x * 1000 * 100,
            "miles": lambda x: x / 1.60934,
            "yards": lambda x: x * 1093.61,
            "feet": lambda x: x * 1093.61 * 3
        }
    },





    
    "temperature": {
        "celsius": {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: 1.8 * x + 32,
            "kelvin": lambda x: x + 273,
        },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celsius": lambda x: (x - 32) * 5.0 / 9.0,
            "kelvin": lambda x: (x - 32) * 5.0 / 9.0 + 273,
        },
        "kelvin": {
            "kelvin": lambda x: x,
            "celsius": lambda x: x - 273,
            "fahrenheit": lambda x: 1.8 * (x - 273) + 32,
        }
    },


    "area": {
        "Squarekm": {
            "Squarekm": lambda x: x,
            "Square metre": lambda x: x*(10**6),
            "Square mile": lambda x: x/2.59,
            "Acre": lambda x: x*(247.105),
        },
        
        "Square metre": {
            "Squarekm": lambda x: x*(10**6),
            "Square metre": lambda x: x,
            "Square mile": lambda x: x/(2.59*(10**6)),
            "Acre": lambda x: x/4046.856,
        },
        
        "Square mile": {
            "Squarekm": lambda x: x*2.59,
            "Square metre": lambda x: x*2.59*(10**6),
            "Square mile": lambda x: x,
            "Acre": lambda x: x*640,
        },

        "Acre": {
            "Squarekm": lambda x: x/247.105,
            "Square metre": lambda x: x*4046.856,
            "Square mile": lambda x: x/640,
            "Acre": lambda x: x,
        }
    },






    "mass": {
        "Metric Ton": {
            "Metric Ton": lambda x: x,
            "Kilogram": lambda x: x*1000,
            "Pound": lambda x: x*2204.62,
            "Gram": lambda x: x*(10**6),
        },
        
        "Kilogram": {
            "Metric Ton": lambda x: x/1000,
            "Kilogram": lambda x: x,
            "Pound": lambda x: x*2.20462,
            "Gram": lambda x: x*1000,
        },
        
        "Pound": {
            "Metric Ton": lambda x: x/2204.623,
            "Kilogram": lambda x: x/2.205,
            "Pound": lambda x: x,
            "Gram": lambda x: x*453.592,
        },

        "Gram": {
            "Metric Ton": lambda x: x/(10**6),
            "Kilogram": lambda x: x/(1000),
            "Pound": lambda x: x/453.592,
            "Gram": lambda x: x,
        }
    },

    "time" : {
        "Second": {
            "Second": lambda x: x,
            "Minute": lambda x: x/60,
            "Hour": lambda x: x/3600,
            "Day": lambda x: x/86400,
            "Month": lambda x: x/(2.62*(10**6)),
            "Year": lambda x: x/(3.154*(10**7)),
        },
        
        "Minute": {
            "Second": lambda x: x*60,
            "Minute": lambda x: x,
            "Hour": lambda x: x/60,
            "Day": lambda x: x/1440,
            "Month": lambda x: x/43800.048,
            "Year": lambda x: x/525600,
        },
        
        "Hour": {
            "Second": lambda x: x*3600,
            "Minute": lambda x: x*60,
            "Hour": lambda x: x,
            "Day": lambda x: x/24,
            "Month": lambda x: x/730.001,
            "Year": lambda x: x/8760,
        },

        "Day": {
            "Second": lambda x: x*86400,
            "Minute": lambda x: x*1440,
            "Hour": lambda x: x*24,
            "Day": lambda x: x,
            "Month": lambda x: x/30.417,
            "Year": lambda x: x/365,
        },

        "Month": {
            "Second": lambda x: x*(2.628(10**6)),
            "Minute": lambda x: x*43800,
            "Hour": lambda x: x*730.001,
            "Day": lambda x: x*30.417,
            "Month": lambda x: x,
            "Year": lambda x: x/12,
        },

        "Year": {
            "Second": lambda x: x*(3.154(10**7)),
            "Minute": lambda x: x*525600,
            "Hour": lambda x: x*8760,
            "Day": lambda x: x*365,
            "Month": lambda x: x*12,
            "Year": lambda x: x,
        }
    }
}











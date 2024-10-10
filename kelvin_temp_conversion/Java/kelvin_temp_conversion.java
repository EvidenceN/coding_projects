public class kelvin_temp_conversion{
  public static void main(String[] args) {
    // The consant value for Kelvin temperature
    int kelvin = 293;

    // The constant value for Celsius
    int celsius = kelvin - 273;
    System.out.println(String.format("The temperature is %s degrees Celsius.", celsius));

    // value for Fahrenheit 
    double Fahrenheit = celsius * ((float)9/5) + 32;
    System.out.println(String.format("The temperature is %s degrees Fahrenheit when not rounded.", Fahrenheit));

    // rounding Fahrenheit
    Fahrenheit = Math.floor(Fahrenheit);

    System.out.println(String.format("The temperature is %s degrees Fahrenheit.", Fahrenheit));

    // Convert temperature to newton scale
    double newton = Math.floor(celsius * ((float)33/100));
    System.out.println(String.format("The temperature when floored is %s degrees newton.", newton));

    float newton_2 = Math.round(celsius * ((float)33/100));
    System.out.println(String.format("The temperature when rounded is %s degrees newton.", newton_2));    

    float newton_3 = celsius * ((float)33/100);
    System.out.println(String.format("The temperature when not rounded is %s degrees newton.", newton_3));        

    float newton_4 = (float)33/100;
    System.out.println(String.format("division test is %s degrees newton.", newton_4));           
  }
 

}
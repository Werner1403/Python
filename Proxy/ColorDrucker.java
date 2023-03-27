public class ColorDrucker implements Drucker {
   @Override
   public void drucken(String dokument) {
       System.out.println("Drucken in Farbe: " + dokument);
   }
}

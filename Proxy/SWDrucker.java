public class SWDrucker implements Drucker {
    @Override
    public void drucken(String dokument) {
        System.out.println("Drucken in Schwarz-Weiß: " + dokument);
    }
}

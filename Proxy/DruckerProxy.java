public class DruckerProxy implements Drucker {
    private Drucker aktuellerDrucker;

    public DruckerProxy(Drucker StandardDrucker) {
        this.aktuellerDrucker = StandardDrucker;
    }

    public void switchTo(Drucker drucker) {
        this.aktuellerDrucker = drucker;
    }

    @Override
    public void drucken(String dokument) {
        if (dokument == "") {
            System.out.println("kein Dokument ausgewählt!");
        } else {
            aktuellerDrucker.drucken(dokument);
        }
    }
}

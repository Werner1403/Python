public class Kunde {
    public static void main(String[] args) {
        DruckerProxy druckerProxy = new DruckerProxy(new SWDrucker());

        druckerProxy.drucken("Dokument 1");

        druckerProxy.switchTo(new ColorDrucker());
        druckerProxy.drucken("Dokument 2");

        druckerProxy.switchTo(new SWDrucker());
        druckerProxy.drucken("Dokument 3");

        druckerProxy.switchTo(new ColorDrucker());
        druckerProxy.drucken("Dokument 4");
        
        druckerProxy.drucken("");
    }
}
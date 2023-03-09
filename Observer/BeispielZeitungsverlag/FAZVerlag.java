package Python.Observer.BeispielZeitungsverlag;

import java.util.ArrayList;
import java.util.List;

public class FAZVerlag{ 

    private List<Abonnent> abonnentenList = new ArrayList<Abonnent>();

    private Zeitung aktuelleZeitung; 


    public void aboHinzufuegen(Abonnent abonnent) { 
        abonnentenList.add(abonnent); 
    } 

    public void aboEntfernen(Abonnent abonnent) { 
        abonnentenList.remove(abonnent); 
    } 

    private void verteileZeitung(Zeitung zeitung) { 
        for (Abonnent abonnent : abonnentenList) { 
            abonnent.erhalteZeitung(zeitung); 
        } 
    } 

    public void setAktuelleZeitung(Zeitung aktuelleZeitung) { 
        this.aktuelleZeitung = aktuelleZeitung; 
        //Nach dem einen neue Zeitung gesetzt wurde, werden alle Abonnenten benachrichtigt. 
        verteileZeitung(aktuelleZeitung); 
    } 

    public Zeitung getAktuelleZeitung() { 
        return aktuelleZeitung; 
    } 
} 
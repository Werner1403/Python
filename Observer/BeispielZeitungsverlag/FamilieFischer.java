package BeispielZeitungsverlag;

class FamilieFischer implements Abonnent { 

    public void erhalteZeitung(Zeitung zeitung) { 
        System.out.println("Familie Fischer erhielt die aktuelle Zeitung: " + zeitung.getTitel()); 
    } 
} 

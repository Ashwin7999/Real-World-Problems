import java.util.*;
import java.util.Map.Entry;

public class Ajira {

    public static List<String> checkConsumption(Map<String, Integer> villageConsumption, Map<String, Integer> villageCapacity) {
        List<String> refill = new LinkedList<>();
        for(Entry<String, Integer> cons : villageConsumption.entrySet()) {
            if(cons.getValue() > villageCapacity.get(cons.getKey())) {
                refill.add(cons.getKey());
            }
        }
        return refill;
    }

    public static void drainClusters(Map<String, Integer> villageConsumption, Map<String, Integer> villageCapacity) {
        for(Entry<String, Integer> cons : villageConsumption.entrySet()) {
            villageCapacity.put(cons.getKey(), (villageCapacity.get(cons.getKey())-cons.getValue()));
        }
    }

    public static int refillClusters(List<String> refill, List<List<String>> pipes, Map<String, Integer> villageCapacity, Map<String, Integer> villageCapacityRefill, int water) {
        for(String s : refill) {
            for(List<String> pipe : pipes) {
                if(pipe.contains(s)) {
                    for(String p : pipe.subList(0,pipe.indexOf(s)+1)) {
                        villageCapacity.put(p,0);
                    }
                }
            }
        }
        for(Entry<String, Integer>  cap : villageCapacity.entrySet()) {
            if(cap.getValue()==0) {
                cap.setValue(villageCapacityRefill.get(cap.getKey()));
                water = water+villageCapacityRefill.get(cap.getKey());
            }
        }
        return water;
    }

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        //Total Number of Days:
        int totalDays = sc.nextInt();
        int water = 0;

        //Villages and Clusters:
        int villageClusterCount = sc.nextInt();
        Map<String, Integer> villageConsumption = new LinkedHashMap<>();
        Map<String, Integer> villageCapacity = new LinkedHashMap<>();
        sc.nextLine();
        for(int i=0;i<villageClusterCount;i++) {
            String[] parts = sc.nextLine().split(" ");
            villageConsumption.put(parts[0], Integer.parseInt(parts[1]));
            villageCapacity.put(parts[0], Integer.parseInt(parts[2]));
            water = water + Integer.parseInt(parts[2]);
        }
        Map<String, Integer> villageCapacityRefill = new LinkedHashMap<>(villageCapacity);

        //Pipe Connections:
        int totalPipes = sc.nextInt();
        sc.nextLine();
        List<List<String>> pipes = new ArrayList<>();
        for(int j=0;j<totalPipes;j++) {
            String[] parts = sc.nextLine().split("_");
            if(parts[0].equals("F")) {
                List<String> newPipe = new ArrayList<>();
                newPipe.add(parts[1]);
                pipes.add(newPipe);
            }
            else {
                for(List<String> pipe : pipes) {
                    if(pipe.contains(parts[0])) {
                        pipe.add(parts[1]);
                    }
                }
            }
        }

        for(int i=0; i<totalDays; i++) {
            List<String> refill = checkConsumption(villageConsumption, villageCapacity);
            if(!refill.isEmpty()) {
                    water = refillClusters(refill,  pipes, villageCapacity, villageCapacityRefill, water);
            }
            drainClusters(villageConsumption, villageCapacity);
        }

        System.out.println("Total Water Consumption for "+totalDays+" days is : "+water);
    }
}
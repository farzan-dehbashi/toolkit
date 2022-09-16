package com.java_tutorial;

import java.util.*;


public class Main {

    public static void main(String[] args) {
        /// Simple arr
        int[] list = new int[12];
        list[1] = 12;
        Arrays.sort(list);
        System.out.println(Arrays.toString(list));
        String[] array = {"1", "2", "3"};

        ///String
        String name = "name";
        boolean isEqual = name.equalsIgnoreCase("name");
        int length = name.length();
        String replace = name.replace("a", "b");
        int index = name.indexOf("a");
        String[] subStrings = name.split("a");
        System.out.println(Arrays.toString(subStrings));

        /// hashmap
        HashMap<Integer, String> hashMap = new HashMap<Integer, String>();
        hashMap.put(1, "one");
        hashMap.put(2, "two");
        System.out.println(hashMap.get(1));
        System.out.println(hashMap.toString());
        hashMap.remove(1);
        System.out.println(hashMap.size());
        // find
        for (Integer key : hashMap.keySet()){ // keySet()
            System.out.println(hashMap.get(key));
        }
        //hashMap.values()

        System.out.println(hashMap.containsKey(1));
        //hashMap.replace(key, newValue);










        /// Array list
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        Collections.addAll(arr,2,3);
        System.out.println(arr);





    }



}

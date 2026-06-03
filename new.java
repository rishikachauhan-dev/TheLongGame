
package org.example;

public class RishikaLesson {
//    public int n;
    private static int getOdd(String s, int i){
        int left=i-1;
        int right=i+1;
        int n=s.length();
        while(left>=0 && right<n){
            if(s.charAt(left)==s.charAt(right)){
                left--;
                right++;
            }
            else break;
        }
        return right-left+1;
    }
    private static int getEven(String s, int i){
        int left=i;
        int right=i+1;
        int n=s.length();
        while(left>=0 && right<n){
            if(s.charAt(left)==s.charAt(right)){
                left--;
                right++;
            }
            else break;
        }
        return right-left+1;
    }
    public static void main(String[] args) {
        String str="aabcxxxabbadd";
        int n=str.length();
        int maxi=0;
        for(int i=0;i<n;i++){
            maxi=Math.max(maxi,Math.max(getOdd(str,i),getEven(str,i)));
        }
        System.out.println(maxi);
    }
}
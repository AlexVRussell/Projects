import java.util.Scanner;

public class Account {
    public static void main(String[] args) {
        Account alex = new Account("Alex Russell", "A1505");
        alex.showMenu();
    }
     int balance;
     int previousTransaction;
     String customerName;
     String customerID;

     Account(String cname, String cid){
         customerName = cname;
         customerID = cid;
     }

     void deposit(int amount){
        if(amount != 0){
            balance = balance + amount;
            previousTransaction = amount;
        }
    }

    void withdraw(int amount){
         if(amount != 0){
             balance = balance - amount;
             previousTransaction = -amount;
         }
    }
    void getPreviousTransaction(){
         if(previousTransaction > 0){
             System.out.println("Deposited: " + previousTransaction);
         }
         else if (previousTransaction < 0){
             System.out.println("Withdrawn: " + Math.abs(previousTransaction));
         }
         else{
             System.out.println("No Transaction occurred");
         }
    }
    void calculateInterest (int years){
        double interestRate = 0.015;
        double newBalance = (balance * interestRate * years) + balance;
        System.out.println("The current interest rate in Canada is " + (interestRate * 100) + "%");
        System.out.println("In " + years + " years, your account balance will be: " + newBalance);
    }
    void showMenu(){
        char option = ' ';
        int years;
         Scanner in = new Scanner(System.in);
         System.out.println("Welcome, " + customerName);
         System.out.println("ID: " + customerID + "\n");
         System.out.println("How can we help you?\nA. Check Balance\nB. Make deposit\nC. Withdraw\nD. View previous \nE. Calculate interest\nF. Exit\nG. Show menu");

         do {
            System.out.println();
            System.out.println("Select an action");
            char option1 = in.next().charAt(0);
            option = Character.toUpperCase(option1);
            System.out.println();

             switch (option) {
                 case 'A' -> {
                     System.out.println("----------------------");
                     System.out.println("Balance: $" + balance);
                     System.out.println("----------------------");
                 }
                 case 'B' -> {
                     System.out.println("How much would you like to deposit?");
                     int amount = in.nextInt();
                     deposit(amount);
                     System.out.println();
                 }
                 case 'C' -> {
                     System.out.println("Enter an amount to withdraw");
                     int amountW = in.nextInt();
                     withdraw(amountW);
                     System.out.println();
                 }
                 case 'D' -> {
                     System.out.println("----------------------");
                     getPreviousTransaction();
                     System.out.println("----------------------");
                 }
                 case 'E' -> {
                     System.out.println("How many years of interest: ");
                     years = in.nextInt();
                     calculateInterest(years);
                 }
                 case 'F' -> {
                     System.out.println("----------------------");
                 }
                 case 'G' -> {
                     System.out.println("How can we help you?\nA. Check Balance\nB. Make deposit\nC. Withdraw\nD. View previous \nE. Calculate interest\nF. Exit\nG. Show menu");
                 }
                 default -> System.out.println("Error: invalid input. Please enter A, B, C, D, E");
             }
         }while(option != 'F');
         System.out.println("Thanks for banking with us!");
     }
}


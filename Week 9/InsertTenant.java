package com.rentpal.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class InsertTenant {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/rentpal";
        String user = "root";
        String password = "your_password";
        String query = "INSERT INTO tenant (name, email, phone_number, remaining_rent, payment_status) VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setString(1, "Aarav Mehta");
            stmt.setString(2, "aarav.mehta@example.com");
            stmt.setString(3, "9876543210");
            stmt.setDouble(4, 8000.0);
            stmt.setString(5, "Pending");

            int rowsInserted = stmt.executeUpdate();
            System.out.println(rowsInserted + " record inserted successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

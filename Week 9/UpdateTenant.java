package com.rentpal.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class UpdateTenant {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/rentpal";
        String user = "root";
        String password = "your_password";
        String query = "UPDATE tenant SET remaining_rent = ?, payment_status = ? WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setDouble(1, 0.0);
            stmt.setString(2, "Paid");
            stmt.setLong(3, 1); // Update tenant with ID = 1

            int rowsUpdated = stmt.executeUpdate();
            System.out.println(rowsUpdated + " record updated successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

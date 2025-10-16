package com.rentpal.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DeleteTenant {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/rentpal";
        String user = "root";
        String password = "your_password";
        String query = "DELETE FROM tenant WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setLong(1, 2); // Delete tenant with ID = 2

            int rowsDeleted = stmt.executeUpdate();
            System.out.println(rowsDeleted + " record deleted successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

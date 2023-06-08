<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%
    String uid=request.getParameter("username");
    String upw=request.getParameter("password");
    String sql="INSERT INTO user_info(username, password) VALUES";
    sql+="('" + uid + "','" + upw + "')";

    Class.forName("com.mysql.jdbc.Driver");
    Connection conn=DriverManager.getConnection("jdbc:mysql://#:3306/#", "#", "#");
    Statement stmt=conn.createStatement();

    int count=stmt.executeUpdate(sql);
    if(count==1){
            response.sendRedirect("login.html");
    }
    else{
            response.sendRedirect("signup.html");
    }
    stmt.close();
    conn.close();
%>

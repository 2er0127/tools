<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%
    String uid=request.getParameter("username");
    String pwd=request.getParameter("password");
    String DB_URL="jdbc:mysql://#:3306/#";
    String DB_USER="#";
    String DB_PASSWORD="#";
    String sel="";
    ResultSet rs=null;
    Connection conn;
    Statement stmt;

    try{
        Class.forName("com.mysql.jdbc.Driver");
        conn=DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
        stmt=conn.createStatement();
        sel="select * from user_info where username='"+uid+"' and password='"+pwd+"'";
        rs=stmt.executeQuery(sel);
        if(rs.next()){
            response.sendRedirect("main.html");
        }
        else
            response.sendRedirect("login.html");
        conn.close();
    } catch(Exception e){
        out.println(e.getMessage());
    }
%>

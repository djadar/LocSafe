import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert'; 
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: PropertyListScreen(),
    );
  }
}

class PropertyListScreen extends StatelessWidget {
  const PropertyListScreen({super.key});

  Future<List<dynamic>> fetchProperties() async {
    final response = await http.get(Uri.parse('http://localhost:5000/properties'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load properties');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Properties')),
      body: FutureBuilder(
        future: fetchProperties(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return CircularProgressIndicator();
          } else if (snapshot.hasError) {
            return Text('Error: ${snapshot.error}');
          } else {
            final properties = snapshot.data as List;
            return ListView.builder(
              itemCount: properties.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(properties[index]['name']),
                  subtitle: Text(properties[index]['address']),
                );
              },
            );
          }
        },
      ),
    );
  }
}


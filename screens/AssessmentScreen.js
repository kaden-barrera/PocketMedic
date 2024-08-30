// screens/AssessmentScreen.js
import React from 'react';
import { View, Text, TextInput, Button, ScrollView } from 'react-native';

const AssessmentScreen = ({ navigation }) => {
  return (
    <ScrollView contentContainerStyle={{ padding: 16 }}>
      <Text style={{ fontSize: 24, marginBottom: 16 }}>Patient Assessment</Text>

      <Text>Symptoms</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 12 }}
        placeholder="Enter symptoms"
      />

      <Text>Heart Rate</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 12 }}
        placeholder="Enter heart rate"
        keyboardType="numeric"
      />

      <Text>Blood Pressure</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 12 }}
        placeholder="Enter blood pressure"
        keyboardType="numeric"
      />

      <Text>Important Notes</Text>
      <TextInput
        style={{ height: 100, borderColor: 'gray', borderWidth: 1, marginBottom: 12 }}
        placeholder="Enter important notes"
        multiline
      />

      <Button
        title="Submit Assessment"
        onPress={() => navigation.navigate('Review')}
      />
    </ScrollView>
  );
};

export default AssessmentScreen;

// screens/ReviewScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';

const ReviewScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 24, marginBottom: 16 }}>Review Assessment</Text>
      <Text>Review the details here...</Text>

      <Button
        title="Submit"
        onPress={() => navigation.navigate('Home')}
      />
    </View>
  );
};

export default ReviewScreen;

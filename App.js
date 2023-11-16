import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';

//Se importa la barra
import Navigation from "./components/Navigation";

//Se importan pantallas
import Login from './screens/Login';
import Registro from './screens/Registro';
//Logeador de usuario
import {UserProvider} from './components/Context/UserProvider';
import { EmailProvider } from './components/Context/EmailProvider';
import { JsonProvider } from './components/Context/JsonProvider';
import { PatientList } from './components/Context/PatientList';
const Stack = createStackNavigator();

export default function App() {
  return (
  <PatientList>
    <JsonProvider>
    <EmailProvider>
    <UserProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Login">
          <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />
          <Stack.Screen name="Registro" component={Registro} options={{ headerShown: false }} />
          <Stack.Screen name="Home" component={Navigation} options={{ headerShown: false }} />
        </Stack.Navigator>
      </NavigationContainer>
    </UserProvider>
    </EmailProvider>
    </JsonProvider>
  </PatientList>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

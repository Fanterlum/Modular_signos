import React, { useState } from "react";
import {
  Text,
  View,
  Image,
  StyleSheet,
  TextInput,
  Button,
  Alert,
  TouchableOpacity,
} from 'react-native'
import { useNavigation } from "@react-navigation/native";
import CustomDropdown from './CustomDropdown.js';

const Registro = () => {
  const options = ['Paciente', 'Doctor', 'Familiar'];

  const navigation = useNavigation();

  const [Nombre, setNombre] = useState('');
  const [Apellidos, setApellidos] = useState('');
  const [Correo, setCorreo] = useState('');
  const [password, setPassword] = useState('');

  const handleRegistro = () => {
    Alert.alert('DATOS REGISTRADOS!!');
    console.log(`\nNombre: ${Nombre}\nApellido: ${Apellidos}\nCorreo: ${Correo}\nContraseña: ${password}\n`);
    navigation.push('Login');
};

  const handleLogin = () => {
    navigation.push('Login');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign Up</Text>
      <TextInput
        style={styles.formulario}
        placeholder="Nombre"
        value={Nombre}
        onChangeText={setNombre}
      />
      <TextInput
        style={styles.formulario}
        placeholder="Apellidos"
        value={Apellidos}
        onChangeText={setApellidos}
      />
      <TextInput
        style={styles.formulario}
        placeholder="tuCorreo@ejemplo.com"
        value={Correo}
        onChangeText={setCorreo}
      />
      <TextInput
        style={styles.formulario}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <View style={styles.dropdown}>
        <CustomDropdown options={options} />
      </View>
      <Button title="Registrarse" onPress={handleRegistro} color='#1C2B2E' />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
      <Text>{'\n'}</Text>
        <Text style={styles.boton_registro}>¿Tienes cuenta? Inicia sesión aquí.</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#B4E2E5',
    padding: 20,
  },
  title: {
    fontSize: 30,
    color: 'black',
    marginBottom: 20,
  },
  formulario: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    backgroundColor: 'white',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10,
    borderRadius: 70,
  },
  boton_registro: {
    fontSize: 17,
    color: '#1C2B2E', // Cambia el color del texto del botón de registro
  },
  dropdown: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    backgroundColor: 'white',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10,
    borderRadius: 70,
  },
});

export default Registro;
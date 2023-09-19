import React, { useState } from "react";
import {
  Text,
  View,
  StyleSheet,
  TextInput,
  Button,
  Alert,
  TouchableOpacity,
  ScrollView, // Usa un ScrollView para manejar contenido desplazable si es necesario
  Dimensions, // Para obtener las dimensiones de la pantalla
} from 'react-native'
import { useNavigation } from "@react-navigation/native";
import { Picker } from '@react-native-picker/picker';

const Registro = () => {
  const navigation = useNavigation();
  const [Nombre, setNombre] = useState('');
  const [Apellidos, setApellidos] = useState('');
  const [Correo, setCorreo] = useState('');
  const [password, setPassword] = useState('');
  const [Cedula, setCedula] = useState('');
  const [Especialidad, setEspecialidad] = useState('');
  const [Tipo_Usuario, setTipo_Usuario] = useState('');
  const [mostrarOpcionesEspeciales, setMostrarOpcionesEspeciales] = useState(
    false
  );
  const [errores, setErrores] = useState({});

  const validarFormulario = () => {
    const errores = {};
  
    if (!Nombre) {
      errores.Nombre = '*El nombre es obligatorio*';
    }
    if (!Apellidos) {
      errores.Apellidos = '*Los apellidos son obligatorios*';
    }
    if (!Correo) {
      errores.Correo = '*El correo es obligatorio*';
    }
    if (!password) {
      errores.password = '*La contraseña es obligatoria*';
    }
    if (Tipo_Usuario === 'Doctor') {
      if (!Cedula) {
        errores.Cedula = '*La cédula es obligatoria*';
      }
      if (!Especialidad) {
        errores.Especialidad = '*La especialidad es obligatoria*';
      }
    }
    if (Tipo_Usuario === null) {
      errores.Tipo_Usuario = '*Por favor, selecciona un tipo de usuario*';
    }
  
    setErrores(errores);
  
    return Object.keys(errores).length === 0; // Devuelve true si no hay errores
  };
  

  const handleRegistro = () => {
    const esFormularioValido = validarFormulario();
  
    if (esFormularioValido) {
      if (!Tipo_Usuario) {
        Alert.alert('Por favor, selecciona un tipo de usuario.');
      } else {
        Alert.alert('DATOS REGISTRADOS!!');
        let datos = `\nNombre: ${Nombre}\nApellido: ${Apellidos}\nCorreo: ${Correo}\nContraseña: ${password}\nTipo Usuario: ${Tipo_Usuario}\n`;
  
        if (Tipo_Usuario === "Doctor") {
          datos += `Cedula: ${Cedula}\nEspecialidad: ${Especialidad}\n`;
        }
  
        console.log(datos);
  
        navigation.push('Login');
      }
    } else {
      Alert.alert('Por favor, completa todos los campos obligatorios.');
    }
  };
  

  const handleLogin = () => {
    navigation.push('Login');
  };

  const handleTipoUsuarioChange = (value) => {
    setTipo_Usuario(value);
    // Si se selecciona "Doctor", mostrar las opciones especiales.
    if (value === "Doctor") {
      setMostrarOpcionesEspeciales(true);
    } else {
      setMostrarOpcionesEspeciales(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Sign Up</Text>
      {errores.Nombre && <Text style={styles.error}>{errores.Nombre}</Text>}
      <TextInput
        style={styles.formulario}
        placeholder="Nombre"
        value={Nombre}
        onChangeText={setNombre}
      />
      {errores.Apellidos && <Text style={styles.error}>{errores.Apellidos}</Text>}
      <TextInput
        style={styles.formulario}
        placeholder="Apellidos"
        value={Apellidos}
        onChangeText={setApellidos}
      />
      {errores.Correo && <Text style={styles.error}>{errores.Correo}</Text>}
      <TextInput
        style={styles.formulario}
        placeholder="tuCorreo@ejemplo.com"
        value={Correo}
        onChangeText={setCorreo}
      />
      {errores.password && <Text style={styles.error}>{errores.password}</Text>}
      <TextInput
        style={styles.formulario}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <View style={styles.dropdown}>
        <Picker
          selectedValue={Tipo_Usuario}
          onValueChange={handleTipoUsuarioChange}
          mode="dropdown"
          style={pickerSelectStyles.estilo}
        >
          <Picker.Item label="Seleccionar tipo de usuario" value={null} />
          <Picker.Item label="Paciente" value={'Paciente'} />
          <Picker.Item label="Doctor" value={'Doctor'} />
          <Picker.Item label="Familiar" value={'Familiar'} />
        </Picker>
      </View>
      {errores.Tipo_Usuario && <Text style={styles.error}>{errores.Tipo_Usuario}</Text>}
      {mostrarOpcionesEspeciales && (
      <View>
          {errores.Cedula && <Text style={styles.error}>{errores.Cedula}</Text>}
          <TextInput
            style={styles.formulario}
            placeholder="Cedula Profesional"
            value={Cedula}
            onChangeText={setCedula}
          />
          {errores.Especialidad && <Text style={styles.error}>{errores.Especialidad}</Text>}
          <TextInput
            style={styles.formulario}
            placeholder="Especialidad"
            value={Especialidad}
            onChangeText={setEspecialidad}
          />
        </View>
      )}
      <Button title="Registrarse" onPress={handleRegistro} color='#1C2B2E' />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text>{'\n'}</Text>
        <Text style={styles.boton_login}>¿Tienes cuenta? Inicia sesión aquí.</Text>
      </TouchableOpacity>
    </ScrollView>
  );
};

const windowWidth = Dimensions.get('window').width;

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#B4E2E5',
    padding: 20,
  },
  title: {
    fontSize: 30,
    color: 'black',
    marginBottom: 20,
    fontWeight: 'bold',
  },
  formulario: {
    width: windowWidth * 0.8, // Utiliza porcentaje en lugar de dimensiones fijas
    height: 40,
    borderColor: 'gray',
    backgroundColor: 'white',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10,
    borderRadius: 70,
  },
  boton_login: {
    fontSize: 17,
    color: '#1C2B2E',
    fontWeight: 'bold',
  },
  dropdown: {
    width: windowWidth * 0.8, // Utiliza porcentaje en lugar de dimensiones fijas
    height: 40,
    borderColor: 'gray',
    backgroundColor: 'white',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10,
    borderRadius: 70,
  },
  error: {
    fontSize: 15,
    color: 'red',
    //marginLeft: 15,
  },
});

const pickerSelectStyles = StyleSheet.create({
  estilo: {
    marginLeft: -15,
    marginVertical: -9,
    fontSize: 12,
  },
});

export default Registro;

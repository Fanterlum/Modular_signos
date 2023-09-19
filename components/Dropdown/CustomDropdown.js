import React, { useState } from 'react';
import { Picker } from '@react-native-picker/picker';
import { StyleSheet } from 'react-native';

const Dropdown = () => {
  const [Tipo_Usuario, setTipo_Usuario] = useState('');

  const handleChangeTipoUsuario = (value) => {
    setTipo_Usuario(value);
    console.log('Tipo_Usuario:', value); // Agrega esta línea para verificar el valor seleccionado
  };

  return (
    <Picker
      selectedValue={Tipo_Usuario}
      //onValueChange={handleChangeTipoUsuario}
      onValueChange={(value) => setTipo_Usuario(value)}
      mode="dropdown"
      style={pickerSelectStyles.estilo}
    >
      <Picker.Item label="Seleccionar tipo de usuario" value={null} />
      <Picker.Item label="Paciente" value={'Paciente'} />
      <Picker.Item label="Doctor" value={'Doctor'} />
      <Picker.Item label="Familiar" value={'Familiar'} />
    </Picker>
  );
};

const pickerSelectStyles = StyleSheet.create({
  estilo: {
    marginLeft: -15,
    marginVertical: -9,
    fontSize: 12,
  },
});

export default Dropdown;

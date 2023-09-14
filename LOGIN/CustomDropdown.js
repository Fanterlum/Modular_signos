/* eslint-disable prettier/prettier */
import React from 'react';
import {useState} from 'react';
import {Picker} from '@react-native-picker/picker';
import {StyleSheet} from 'react-native';


export default function Form(props) {
  const [Tipo_Usuario, setTipo_Usuario] = useState('');
  
    return (
      <Picker
        selectedValue={Tipo_Usuario}
        onValueChange={(value) => setTipo_Usuario(value)}
        mode="dropdown"
        style={pickerSelectStyles.estilo}
        >
        <Picker.Item label="Seleccionar tipo de usuario" value={null}/>
        <Picker.Item label="Paciente" value={'Paciente'} />
        <Picker.Item label="Doctor" value={'Doctor'} />
        <Picker.Item label="Familiar" value={'Familiar'} />
      </Picker>
    );
}


const pickerSelectStyles = StyleSheet.create({
  estilo: {
    marginLeft: -15,
    marginVertical: -9,
    fontSize: 12,
  },
});
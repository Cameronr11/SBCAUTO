"use client";
import React, { useState } from 'react';
import { Box, FormControl, FormLabel, Input, SimpleGrid, ChakraProvider } from '@chakra-ui/react';

const positions: string[] = ['GK', 'CB', 'LB', 'RB', 'LWB', 'RWB', 'CM', 'CDM', 'CAM', 'CF', 'ST', 'LM', 'RM', 'RW', 'LW'];

interface FormationComponentProps {
  onFormationChange: (newFormation: { [key: string]: number }) => void;
}

const FormationComponent: React.FC<FormationComponentProps> = ({ onFormationChange }) => {
  const [positionCounts, setPositionCounts] = useState<{ [key: string]: string }>(() => {
    const initialCounts: { [key: string]: string } = {};
    positions.forEach(position => { initialCounts[position] = '0'; }); // Initialize with '0'
    return initialCounts;
  });

  const [isFocused, setIsFocused] = useState<{ [key: string]: boolean }>(() => {
    const initialFocus: { [key: string]: boolean } = {};
    positions.forEach(position => { initialFocus[position] = false; });
    return initialFocus;
  });

  const handleFocus = (position: string) => {
    setIsFocused(prev => ({ ...prev, [position]: true }));
    if (positionCounts[position] === '0') {
      setPositionCounts(prevCounts => ({ ...prevCounts, [position]: '' }));
    }
  };

  const handleBlur = (position: string) => {
    setIsFocused(prev => ({ ...prev, [position]: false }));
    if (positionCounts[position] === '') {
      setPositionCounts(prevCounts => ({ ...prevCounts, [position]: '0' }));
    }
  };

  const handleChange = (position: string, value: string) => {
    const newValue = value.replace(/\D/g, ''); // Allow only digits
    setPositionCounts(prevCounts => {
      const updatedCounts = { ...prevCounts, [position]: newValue || '0' };
      onFormationChange(Object.keys(updatedCounts).reduce((acc, key) => ({
        ...acc,
        [key]: parseInt(updatedCounts[key], 10) || 0
      }), {}));
      return updatedCounts;
    });
  };

  return (
    <ChakraProvider>
      <Box p={4} color="white">
        <SimpleGrid columns={2} spacing={4}>
          {positions.map(position => (
            <FormControl key={position}>
              <FormLabel>{position}:</FormLabel>
              <Input
                type="text"
                name={position}
                value={isFocused[position] ? positionCounts[position] : (positionCounts[position] === '0' ? '' : positionCounts[position])}
                onChange={e => handleChange(position, e.target.value)}
                onFocus={() => handleFocus(position)}
                onBlur={() => handleBlur(position)}
                borderColor="blue.500"
                _hover={{ borderColor: "blue.600" }}
                focusBorderColor="blue.700"
              />
            </FormControl>
          ))}
        </SimpleGrid>
      </Box>
    </ChakraProvider>
  );
};

export default FormationComponent;







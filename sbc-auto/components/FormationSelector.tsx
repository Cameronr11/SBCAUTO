"use client";
import React, { useState } from 'react';
import { Box, FormControl, FormLabel, Input, SimpleGrid, ChakraProvider } from '@chakra-ui/react';

const positions: string[] = ['GK', 'CB', 'LB', 'RB', 'LWB', 'RWB', 'CM', 'CDM', 'CAM', 'CF', 'ST', 'LM', 'RM', 'RW', 'LW'];

const FormationComponent = () => {
  const [positionCounts, setPositionCounts] = useState<{ [key: string]: string }>(() => {
    const initialCounts: { [key: string]: string } = {};
    positions.forEach(position => { initialCounts[position] = '0'; });
    return initialCounts;
  });

  const handleChange = (position: string, value: string) => {
    // Use regular expression to remove non-digit characters
    const newValue = value.replace(/\D/, ''); 
    setPositionCounts(prevCounts => ({ ...prevCounts, [position]: newValue }));
  };

  return (
    <ChakraProvider>
      <Box p={4} color="white">
        <SimpleGrid columns={2} spacing={4}>
          {positions.map(position => (
            <FormControl key={position}>
              <FormLabel>{position}:</FormLabel>
              <Input
                type="text" // Change type to text to allow typing any characters
                name={position}
                value={positionCounts[position]}
                onChange={e => handleChange(position, e.target.value)}
                placeholder="0"
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



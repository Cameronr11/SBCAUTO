"use client";
import { Box, Text, Center, VStack, Spinner } from '@chakra-ui/react';
import React, { useState, useCallback, useEffect } from 'react';
import FormationSelector from "@/components/FormationSelector";
import CriteriaComponent from "@/components/CriteriaComponent";
import CustomButton from "@/components/CustomButton";
import { SBCOptions } from "@/components/CriteriaComponent";

interface Player {
  position: string;
  name: string;
  rating: number;
  league: string;
  club: string;
  nation: string;
  chemistry: number;
}

interface SquadSolution {
  best_squad: Player[];
  best_squad_fitness: number;
  total_chemistry: number;
}

interface Formation {
  [key: string]: number;
}

interface Criteria {
  id: string;
  type: string;
  value: string | number;
}

export type SBCOption = {
  id: number;
  value: string;
  label: string;
};

interface FormationSelectorProps {
  onFormationChange: (newFormation: Formation) => void;
}

const SolverPage = () => {
  const [formation, setFormation] = useState<Formation>({});
  const [criteria, setCriteria] = useState<Criteria[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [squadSolution, setSquadSolution] = useState<SquadSolution | null>(null);


  // useEffect hook for setting the background color
  useEffect(() => {
    const originalBackgroundColor = document.body.style.backgroundColor;
    document.body.style.backgroundColor = 'black';

    // Reset the background color when the component unmounts
    return () => {
      document.body.style.backgroundColor = originalBackgroundColor;
    };
  }, []);


  const handleSolveClick = async () => {
    setLoading(true);
    const criteriaPayload = criteria.reduce<{ [key: string]: string | number }>((acc, curr) => {
      const option = SBCOptions.find((option: SBCOption) => option.value === curr.type);
      if (option) {
        acc[option.id.toString()] = curr.value;
      }
      return acc;
    }, {});


    const formationArray = Object.entries(formation).reduce<string[]>((acc, [position, count]) => {
      if (count > 0) {
        acc.push(...Array(count).fill(position));
      }
      return acc;
    }, []);

    const payload = {
      formation: formationArray,
      criteria: criteriaPayload, // Ensure criteriaPayload is constructed as required
    };

    console.log("Sending payload to backend:", payload);


    try {
      const response = await fetch('http://localhost:5000/solve-SBC', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const responseData: SquadSolution = await response.json();
      setSquadSolution(responseData);
    } catch (error) {
      console.error("Failed to solve SBC:", error);
    } finally {
      setLoading(false);
    }
  };

  const updateCriteria = useCallback((newCriteria: Criteria[]) => {
    setCriteria(newCriteria.map(crit => ({ id: crit.id, type: crit.type, value: crit.value }))); // This ensures criteria state is updated correctly
  }, []);


  return (
    <Box bg="black" color="white" minH="100vh" p={5} display="flex" flexDirection="column" alignItems="center" justifyContent="center">
      {loading ? (
        <Center minH="100vh">
          <Spinner size="xl" />
        </Center>
      ) : squadSolution ? (
        <>
          <Text fontSize="xx-large" color="green.400" fontWeight="bold" mb={6}>SQUAD SOLUTION:</Text>
          <VStack spacing={4}>
            {squadSolution.best_squad.map((player, index) => (
              <Text key={index} color="white" fontSize="lg">{player.name}, {player.rating}</Text>
            ))}
          </VStack>
        </>
      ) : (
        <>
          <Center position="absolute" top="5%" left="50%" transform="translateX(-50%)">
            <Text className='text-white text-3xl md:text-5xl font-bold mb-6'>Build Your SBC</Text>
          </Center>
  
          <Box position="absolute" top="20%" left="10%">
            <Text mb={4} fontSize="2xl" color="blue.400" fontWeight="bold">Specify # of Players Per Position:</Text>
            <FormationSelector onFormationChange={(newFormation) => setFormation(newFormation)} />
          </Box>

  
          <Box position="absolute" top="20%" right="10%">
            <Text mb={4} fontSize="2xl" color="blue.400" fontWeight="bold">Choose SBC Criteria:</Text>
            <CriteriaComponent onCriteriaChange={updateCriteria} />
          </Box>

          <Box position="absolute" top="20%" left="10%">
            <Text mb={4} fontSize="2xl" color="blue.400" fontWeight="bold">Specify # of Players Per Position:</Text>
            <FormationSelector onFormationChange={(newFormation) => setFormation(newFormation)} />
          </Box>
  
          <Center position="absolute" bottom="10%" left="50%" transform="translateX(-50%)">
            <CustomButton
              title="Solve"
              btnType="button"
              containerStyles="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              handleClick={handleSolveClick}
            />
          </Center>
        </>
      )}
    </Box>
  );
}
export default SolverPage;
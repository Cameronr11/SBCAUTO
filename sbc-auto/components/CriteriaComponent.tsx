"use client";
import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Select, Input, Stack, IconButton, ChakraProvider, Button } from '@chakra-ui/react';
import { AddIcon, MinusIcon } from '@chakra-ui/icons';

interface Criteria {
  id: string;
  type: string;
  values: (string | number)[];
}

interface Props {
  onCriteriaChange: (criteria: Criteria[]) => void;
}

export const SBCOptions = [
  { id: 1, value: 'teamRating', label: 'Team Rating: Min. (X)' },
  { id: 2, value: 'totwMinPlayers', label: 'Team of the Week: Min. (X) Player(s)' },
  { id: 3, value: 'minXPlayers', label: '(X): Min. (X) Player(s)' },
  { id: 4, value: 'squadPlayersNumber', label: 'Number of Players in the Squad: (X)' },
  { id: 5, value: 'sameLeagueMax', label: 'Players from the same League: Max (X)' },
  { id: 6, value: 'sameClubMax', label: 'Players from the same Club: Max (X)' },
  { id: 7, value: 'minRarePlayers', label: 'Rare: Min. (X) Players' },
  { id: 8, value: 'minLeagues', label: 'Leagues in Squad: Min. (X)' },
  { id: 9, value: 'minClubs', label: 'Clubs in Squad: Min. (x)' },
  { id: 10, value: 'minGoldPlayers', label: 'Gold: Min. (X) Players' },
  { id: 11, value: 'minSilverPlayers', label: 'Silver: Min. (X) Players' },
  { id: 12, value: 'minBronzePlayers', label: 'Bronze: Min. (X) Players' },
  { id: 13, value: 'minXPlayersGeneric', label: '(X) : Min. (X) Players' },
  { id: 14, value: 'minOvrPlayers', label: 'Players with minimum OVR of (X): Min.(X)' },
  { id: 15, value: 'clubsXorYMinPlayers', label: '"Clubs" (X) or (X): Min. (X) Player(s)' },
  { id: 16, value: 'minNationalities', label: 'Nationalities in Squad: Min. (X)' },
  { id: 17, value: 'exactPlayerQuality', label: 'Player Quality: Exactly (X)' },
  { id: 18, value: 'minTotalChemistry', label: 'Total Chemistry: Min. (X)' },
  { id: 19, value: 'minChemistryPointsPlayer', label: 'Chemistry Points on Each Player: Min.(X)' },
  { id: 20, value: 'minXPlayersGeneric2', label: '(X): Min. (X) Players' },
  { id: 21, value: 'nationsXorYMinPlayers', label: '"Nations" (X) or (X): Min. (X) Player(s)' },
  { id: 22, value: 'leaguesXorYMinPlayers', label: '"Leagues" (X) or (X): Min. (X) Player(s)' },
];

const CriteriaComponent: React.FC<Props> = ({ onCriteriaChange }) => {
  const [criteriaList, setCriteriaList] = useState<Criteria[]>([{ id: uuidv4(), type: '', values: [''] }]);

  const handleCriteriaTypeChange = (id: string, type: string) => {
    setCriteriaList(prev => prev.map(c => c.id === id ? { ...c, type, values: [''] } : c));
  };

  const handleValueChange = (id: string, value: string, index: number) => {
    setCriteriaList(prev => prev.map(c => c.id === id ? { ...c, values: c.values.map((val, idx) => idx === index ? value : val) } : c));
  };

  const addValue = (id: string) => {
    setCriteriaList(prev => prev.map(c => c.id === id ? { ...c, values: [...c.values, ''] } : c));
  };

  const removeValue = (id: string, index: number) => {
    setCriteriaList(prev => prev.map(c => c.id === id ? { ...c, values: c.values.filter((_, idx) => idx !== index) } : c));
  };

  const addCriteria = () => {
    setCriteriaList([...criteriaList, { id: uuidv4(), type: '', values: [''] }]);
  };

  return (
    <ChakraProvider>
      <Stack spacing={4}>
        {criteriaList.map((criterion, index) => (
          <Stack key={criterion.id} direction="row" alignItems="center">
            <Select
              placeholder="Select Criteria"
              value={criterion.type}
              onChange={(e) => handleCriteriaTypeChange(criterion.id, e.target.value)}
              sx={{
                option: {
                  color: 'black', // Ensure text color is always visible
                  backgroundColor: 'white', // Optional: Adjust if you have a specific bg color
                },
              }}
            >
              {SBCOptions.map(option => (
                <option key={option.id} value={option.value}>{option.label}</option>
              ))}
            </Select>
            {criterion.values.map((value, idx) => (
              <Stack key={idx} direction="row" alignItems="center">
                <Input
                  placeholder="Value"
                  value={value.toString()}
                  onChange={(e) => handleValueChange(criterion.id, e.target.value, idx)}
                />
                {idx > 0 && (
                  <IconButton aria-label="Remove value" icon={<MinusIcon />} onClick={() => removeValue(criterion.id, idx)} />
                )}
              </Stack>
            ))}
            {criterion.type && (
              <Button onClick={() => addValue(criterion.id)}>Add Value</Button>
            )}
            {index === criteriaList.length - 1 && (
              <IconButton aria-label="Add criteria" icon={<AddIcon />} onClick={addCriteria} />
            )}
          </Stack>
        ))}
      </Stack>
    </ChakraProvider>
  );
};

export default CriteriaComponent;
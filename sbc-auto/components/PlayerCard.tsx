import { Box, Text, VStack } from '@chakra-ui/react';

interface Player {
  position: string;
  name: string;
  rating: number;
  league: string;
  club: string;
  nation: string;
}

const PlayerCard: React.FC<{ player: Player; index: number }> = ({ player, index }) => {
  // Using a darker shade of blue for better text visibility
  return (
    <Box
      className="bg-blue-500 border-2 border-blue-700 rounded-lg p-4 mb-4 shadow-xl hover:bg-blue-600 text-white"
      _hover={{ boxShadow: "2xl" }}
    >
      <VStack align="start" spacing={2}>
        <Text className="font-bold">({index + 1}) {player.name}</Text>
        <Text>Rating: {player.rating}</Text>
        <Text>League: {player.league}</Text>
        <Text>Nation: {player.nation}</Text>
        <Text>Club: {player.club}</Text>
      </VStack>
    </Box>
  );
};

export default PlayerCard;











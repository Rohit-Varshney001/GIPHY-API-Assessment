import React, { useState, useEffect } from "react";
import axios from "axios";

const GiphyApp = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [gifs, setGifs] = useState([]);

  useEffect(() => {
    fetchGifs();
  }, []);

  const fetchGifs = async (query = "") => {
    try {
      const response = await axios.get(
        `http://localhost:8080/api/gifs?search=${query}`  // Use backticks here
      );
      setGifs(response.data);
    } catch (error) {
      console.error("Error Fetching GIFs:", error);
    }
  };

  const handleSearch = () => {
    fetchGifs(searchTerm);  // Call fetchGifs with the current search term
  };

  return (
    <div className="p-4 text-center">
      <h1 className="text-2xl font-bold mb-4">Giphy Search</h1>
      <input
        type="text"
        placeholder="Search GIFs..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="border p-2"
      />
      <button
        onClick={handleSearch}
        className="ml-2 p-2 bg-blue-500 text-white"
      >
        Search
      </button>
      <div className="grid mt-4">
        {gifs.map((gif) => (
          <img key={gif.id} src={gif.url} alt="GIF" className="w-full" />
        ))}
      </div>
    </div>
  );
};

export default GiphyApp;

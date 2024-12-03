import axios from "axios";
import apiClient from "@/services/api";


/*export async function fetchBars() {
  try {
    const response = await axios.get("/api/fetch-bars");
    return response.data.bars;
  } catch (error: any) {
    throw new Error(
      error.response?.data?.message || "Failed to fetch bars"
    );
  }
} */
export const fetchBars = () => {
    return apiClient.get('/fetch-bars', {
    });
};
import { z } from 'zod';

/**
 * Zod schemas shared between the frontend and backend.
 *
 * These schemas mirror the JSON structures defined in the product
 * specification.  They can be used for runtime validation as well as
 * generating TypeScript types via `z.infer`.  When you modify the
 * Pydantic schemas on the backend ensure the corresponding Zod schemas
 * here are kept in sync.
 */

export const RequirementItemSchema = z.object({
  type: z.string(),
  label: z.string(),
  value: z.string().optional(),
  confidence: z.number().min(0).max(1),
  source_ref: z.string(),
  status: z.string().optional(),
});

export type RequirementItem = z.infer<typeof RequirementItemSchema>;

export const RequirementResponseSchema = z.object({
  tender_id: z.string(),
  requirements: z.array(RequirementItemSchema),
});

export type RequirementResponse = z.infer<typeof RequirementResponseSchema>;

export const AnswerPlanSchema = z.object({
  tender_id: z.string(),
  question_id: z.string(),
  question: z.string(),
  structure: z.array(z.string()),
  evidence_prompts: z.array(z.string()),
  word_limit: z.number().int().optional(),
  weight: z.number().int().optional(),
});

export type AnswerPlan = z.infer<typeof AnswerPlanSchema>;

export default {
  RequirementItemSchema,
  RequirementResponseSchema,
  AnswerPlanSchema,
};